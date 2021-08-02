# 入れ子で引き算、setでかぶりを消して、sorted,reverseで降順にし、0番を出す
N = int(input())
A = list(map(int, input().split()))
sub = []

for i in A:
    for j in A:
        sub.append(abs(i - j))

descending_sub = sorted(set(sub), reverse=True)
# print(descending_sub)

print((descending_sub[0]))
