N = int(input())
S = input()
list1 = []
for i in range(N):
    x = set()
    for s in S[:i + 1]:
        if s in S[i + 1:]:
            x.add(s)
    list1.append(len(x))
print(max(list1))
