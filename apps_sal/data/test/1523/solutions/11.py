from itertools import zip_longest
from operator import itemgetter


def persuade(idler_nos, job_nos, job_chosen, idlers_persuade_time):
    persuade_time = 0
    job_chosen_nos = 0
    job_item_chosen = {}
    job_tuples = sorted(list(zip_longest(job_chosen, idlers_persuade_time)), key=itemgetter(1), reverse=True)
    remain_tuples = []
    for t in job_tuples:
        if t[0] not in job_item_chosen:
            job_item_chosen[t[0]] = 0
            job_chosen_nos += 1
        else:
            remain_tuples.append(t)
            pass
    idler_needed_nos = job_nos - job_chosen_nos
    for i in reversed(list(range(len(remain_tuples) - idler_needed_nos, len(remain_tuples)))):
        persuade_time += remain_tuples[i][1]
    return persuade_time


(idler_nos, job_nos) = list(map(int, input().split()))
job_chosen = list(map(int, input().split()))
idlers_persuade_time = list(map(int, input().split()))
print('{}'.format(persuade(idler_nos, job_nos, job_chosen, idlers_persuade_time)))
