K = int(input())
if K % 2 != 0:
    odd = int((K + 1) / 2)
    even = int((K - 1) / 2)
else:
    odd = int(K / 2)
    even = int(K / 2)
print(odd * even)
