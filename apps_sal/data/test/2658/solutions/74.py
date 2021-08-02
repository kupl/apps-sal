N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

now = 1
route = []
dic = {}
cnt = 0
entry = []
loop = []

while True:
    cnt += 1
    now = A[now]
    route.append(now)
    if now in dic:
        entry = route[:dic[now]]
        loop = route[dic[now]:]
        break
    dic[now] = cnt

if K <= len(entry):
    print(entry[K - 1])
else:
    K -= 1
    K -= len(entry)
    K %= len(loop)
    print(loop[K])
