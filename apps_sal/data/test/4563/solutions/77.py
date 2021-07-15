n = int(input())
t_i,a_i = map(int,input().split())
t = []
a = []
t.append(t_i)
a.append(a_i)
for i in range(1,n):
    t_i,a_i = map(int,input().split())
    t.append(t_i)
    a.append(a_i)
    if t[i-1]>t[i] or a[i-1]>a[i]:
        t_max = t[i-1]//t[i]
        if t[i-1]%t[i]!=0:
            t_max += 1
        a_max = a[i-1]//a[i]
        if a[i-1]%a[i]!=0:
            a_max += 1
        bai = max(t_max,a_max)
        t[i] *= bai
        a[i] *= bai
print(t[-1]+a[-1])
