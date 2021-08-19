a = [0] * 5
for i in range(5):
    a[i] = int(input())
k = int(input())
if a[-1] - a[0] > k:
    s = 0
else:
    s = 1
print([':(', 'Yay!'][s])
