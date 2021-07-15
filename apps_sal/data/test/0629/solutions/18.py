n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
b = list(map(int, input().split()))

pref1 = [0] * n
for i in range(1, n):
    pref1[i] = pref1[i - 1] + a1[i - 1]
pref2 = [0] * n
for i in range(1, n):
    pref2[i] = pref2[i - 1] + a2[i - 1]
post2 = [sum(a2)] * n
for i in range(n):
    post2[i] -= pref2[i]

minimum = -1
for i in range(n):
    for j in range(n):
        if j != i:
            if minimum == -1:
                minimum = pref1[i] + post2[i] + b[i] + pref1[j] + post2[j] + b[j]
            else:
                minimum = min(pref1[i] + post2[i] + b[i] + pref1[j] + post2[j] + b[j], minimum)
print(minimum)

