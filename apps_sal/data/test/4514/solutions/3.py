n, q = map(int, input().split())
sups = list(map(int, input().split()))

dir_subs = [[] for i in range(n + 1)]
num_subs = [0] * (n + 1)

sups = [0, 0] + sups
for i in range(2, n + 1):
    dir_subs[sups[i]].append(i)

prev_parent = 0
qe = [1]
ordered = []

while len(qe) > 0:
    new = qe.pop()

    if new > 0:
        ordered.append(new)

        qe.append(-new)
        num = len(dir_subs[new])
        for i in range(num):
            qe.append(dir_subs[new][num - 1 - i])

    else:
        parent = -new
        for child in dir_subs[parent]:
            num_subs[parent] += 1
            num_subs[parent] += num_subs[child]


indices = [0] * (n + 1)

for i in range(n):
    indices[ordered[i]] = i


def ans_query(u, k):
    if k - 1 > num_subs[u]:
        return -1

    start = indices[u]
    end = ordered[start + k - 1]
    return end


s = ''
for i in range(q):
    u, k = map(int, input().split())
    s += (str(ans_query(u, k)) + '\n')
    if i % 20 == 0:
        print(s[:-1])
        s = ''

if len(s) > 0:
    print(s[:-1])
