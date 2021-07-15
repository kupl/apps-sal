import heapq, itertools, sys
NEGINF = -sys.maxsize

n, m = map(int, sys.stdin.readline().split())
skills_of_subject = {}
for i in range(1, m + 1):
    skills_of_subject[i] = []
for i in range(n):
    s, r = map(int, sys.stdin.readline().split())
    skills_of_subject[s].append(r)

cumul_subject_score_for_n_participants = {s : list(itertools.accumulate(sorted(skills_of_subject[s], key=lambda x: -x))) for s in skills_of_subject.keys()}


subject_with_atleast_nparts = {0 : skills_of_subject.keys()}
for i in range(1, n + 1):
    subject_with_atleast_nparts[i] = list(filter(lambda sid : len(skills_of_subject[sid]) >= i, subject_with_atleast_nparts[i - 1]))
#subject_with_atleast_nparts = {i : list(filter(lambda sid : len(skills_of_subject[sid]) >= i, skills_of_subject.keys())) for i in range(1, n + 1)}

curr_max = 0
for nParticipants in range(1, n+1):
    subject_army_by_competence = sorted([cumul_subject_score_for_n_participants[s][nParticipants - 1] for s in subject_with_atleast_nparts[nParticipants]], key=lambda x: -x)
    total_competence = 0
    for i in range(len(subject_army_by_competence)):
        total_competence += subject_army_by_competence[i]
        curr_max = max(curr_max, total_competence)

print (curr_max)
