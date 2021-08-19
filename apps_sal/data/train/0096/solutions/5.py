t = int(input())
for _ in range(t):
    (n, T, a, b) = list(map(int, input().split(' ')))
    task_t = list(map(int, input().split(' ')))
    ness = list(map(int, input().split(' ')))
    perm = sorted(list(range(n)), key=lambda i: ness[i])
    score = 0
    tot_hard = sum(task_t)
    tot_easy = n - tot_hard
    must_easy = 0
    must_hard = 0
    for i in range(n):
        if i > 0 and ness[perm[i]] == ness[perm[i - 1]]:
            if task_t[perm[i]] == 0:
                must_easy += 1
            else:
                must_hard += 1
            continue
        tm = ness[perm[i]] - 1
        req_time = must_easy * a + must_hard * b
        if req_time > tm:
            if task_t[perm[i]] == 0:
                must_easy += 1
            else:
                must_hard += 1
            continue
        extra_time = tm - req_time
        extra_easy = min(extra_time // a, tot_easy - must_easy)
        extra_time -= a * extra_easy
        extra_hard = min(extra_time // b, tot_hard - must_hard)
        score = max(score, extra_easy + extra_hard + must_easy + must_hard)
        if task_t[perm[i]] == 0:
            must_easy += 1
        else:
            must_hard += 1
    if tot_easy * a + tot_hard * b <= T:
        score = n
    print(score)
