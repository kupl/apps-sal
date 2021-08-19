def val(a, action):
    res = 1000
    if a == 3:
        res = 0
    elif a == 1 and action == 'C':
        res = 0
    elif a == 2 and action == 'G':
        res = 0
    return res


n = int(input())
a = list(map(int, input().split()))
curr = {}
prev = {'G': 0, 'C': 0, 'R': 0}
for i in a:
    curr['G'] = min(prev['C'], prev['R']) + val(i, 'G')
    curr['C'] = min(prev['G'], prev['R']) + val(i, 'C')
    curr['R'] = min(prev['C'], prev['G'], prev['R']) + 1
    prev = curr.copy()
print(min(prev.values()))
