# kitten
f, y, t = map(int, input().split())
cnt = [0] * y
for i in range(0, f):
    s = input()
    for j in range(0, y): cnt[j] += s[j] == 'Y'
print(len([x for x in cnt if x >= t]))
