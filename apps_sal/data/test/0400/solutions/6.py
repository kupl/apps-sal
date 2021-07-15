n, k = [int(i) for i in input().split()]
skills = [int(i) for i in input().split()]
def fornextlvl(x):
    return 10*(1+((x-1)//10))-x
left = sorted([(fornextlvl(skills[i]), i) for i in range(n)])
left.reverse()

while k > 0 and len(left):
    w = left.pop()
    if w[0] > k: break
    k -= w[0]
    skills[w[1]] += w[0]
# Every skill must be a multiple of 10 by now 

for i in range(n):
    t = min(k, (100-skills[i]))
    skills[i] += t
    k -= t
    if k == 0: break

print(sum([i//10 for i in skills]))
