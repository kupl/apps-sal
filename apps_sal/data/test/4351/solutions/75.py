n = int(input())

x = n//100 + n//10%10*10 + n%10*100

print('Yes' if x == n else 'No')
