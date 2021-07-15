n = int(input())
a = list(input())

for i in range(len(a)):
    a[i] = int(a[i])
s = sum(a)

for i in range(2, n+1):
    if s % i == 0:
        b = s // i

        t_sum = 0
        t_k = 0
        for k in a:
            if t_k > i:
                break
            t_sum += k
            if t_sum < b:
                continue
            elif t_sum == b:
                t_sum = 0
                t_k += 1
                continue
            else:
                break
        if t_k == i:
            print("YES")
            return

print("NO")
          
        

