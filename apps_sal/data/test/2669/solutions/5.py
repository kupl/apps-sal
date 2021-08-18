n = int(input())
s = list(map(int, input().split()))
f = list(map(int, input().split()))
t = list(map(lambda x, y: (x, y), s, f))
end = 0
tt = []
k = 0
for i, j in t:
    if(not (tt)):
        tt.append(k)
        end = j
        k += 1
        continue
    if(i >= end):
        tt.append(k)
        end = j
    k += 1
for i in tt:
    print(i, end=" ")
print()
