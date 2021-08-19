(n, k) = list(map(int, input().split()))
ques = []
last = [-1] * (n + 2)
last[0] = 10000000
last[n + 1] = 10000000
frst = [-1] * (n + 2)
ques = input().split()
for i in range(len(ques)):
    ques[i] = int(ques[i])
ans = n * 3
for i in range(k):
    if frst[ques[i]] == -1:
        frst[ques[i]] = i
    last[ques[i]] = i
    'try:\n        if frst[ques[k]] > k :\n            frst[ques[k]] = k    \n        if last[ques[k]] < k :\n            last[ques[k]] = k    \n    except :\n        print(("k : {}".format(k)))'
    'for x in range(1 , n+1) :\n        if last[x] == int(-1) :\n            print(x)\n            frst[x] = -1\n            last[x] = 10000000'
cnt = 0
for i in range(1, n + 1):
    if frst[i] != -1:
        if frst[i] < last[i - 1]:
            cnt += 1
        if frst[i] < last[i + 1]:
            cnt += 1
        if frst[i] != -1:
            cnt += 1
if frst[1] == -1:
    cnt += 1
if frst[n] == -1:
    cnt += 1
ans = ans - cnt
print(ans)
