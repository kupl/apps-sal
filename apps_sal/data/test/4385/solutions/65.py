lists = []
for _ in range(5):
    lists.append(int(input()))
k = int(input())

lists.sort()
maximum = lists[-1]
minimum = lists[0]

if k < maximum - minimum:
    ans = ':('
else:
    ans = 'Yay!'

print(ans)
