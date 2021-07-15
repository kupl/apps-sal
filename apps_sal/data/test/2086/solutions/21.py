h = int(input())
ppl = [int(x) for x in input().split()]
sl = [int(x) for x in input().split()]
n = sl[1] - sl[0] if sl[1] > sl[0] else sl[1] - sl[0] + h
m = 0
index = 0
temp = sum(ppl[0:n])
ans = []
for i in range(h):
    if m < temp:
        m = temp 
        ans.clear()
        ans.append(i)
    elif m == temp:
        ans.append(i)
    temp -= ppl[i]
    temp += ppl[(i+n) % h]
res = [(sl[0] + h - index - 1) % h + 1  for index in ans]
# print(n)
# print(m)
print(min(res))

    

