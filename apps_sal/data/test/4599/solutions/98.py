import numpy as np

n = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)
a = np.array(a)
num_i_even = [i for i in range(n) if i%2==0]
num_i_odd = [i for i in range(n) if i%2!=0]

sum1 = np.sum(a[num_i_even])
sum2 = np.sum(a[num_i_odd])

print(sum1-sum2)
