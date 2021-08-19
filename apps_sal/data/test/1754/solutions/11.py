(n, m, k) = map(int, input().split())
students = list(map(int, input().split()))
schools = list(map(int, input().split()))
v = list(map(int, input().split()))
school_stud = [[] for i in range(max(schools) + 1)]
for i in range(len(schools)):
    school_stud[schools[i]].append((students[i], i))
for i in range(len(school_stud)):
    school_stud[i].sort()
count = 0
for i in range(len(v)):
    if school_stud[schools[v[i] - 1]][-1][1] != v[i] - 1:
        count += 1
print(count)
