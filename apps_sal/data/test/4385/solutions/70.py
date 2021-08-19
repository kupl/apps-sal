l = []
flg = False
for i in range(5):
    l.append(int(input()))
k = int(input())
l.sort(reverse=True)
for i in range(len(l)):
    for j in range(len(l) - i):
        if l[i] - l[j] > k:
            flg = True
print(':(' if flg else 'Yay!')
