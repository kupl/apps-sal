3

n, k = [int(x) for x in input().split()]

t = input()
max_prefix = ''

for i in range(1, len(t)):
    l = t[-i:]
    # print(str(i) + " : " + l)
    if(t.startswith(l)):
        max_prefix = l

# print("Max prefix :- " + max_prefix)

s = ''

if len(max_prefix) == 0:
    for i in range(k):
        s = s + t
else:
    p = t[:n - len(max_prefix)]
    for i in range(k - 1):
        s = s + p
    s = s + t

print(s)
