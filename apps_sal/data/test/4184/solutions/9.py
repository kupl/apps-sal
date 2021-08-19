n = int(input())
wlist = list(map(int, input().split(' ')))
w_sum = sum(wlist)
fw = 0
mind_fb = w_sum
for i in range(n - 1):
    fw += wlist[i]
    bw = w_sum - fw
    d_fb = abs(fw - bw)
    if d_fb < mind_fb:
        mind_fb = d_fb
print(mind_fb)
