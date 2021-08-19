n = int(input())
a = ['012', '102', '120', '210', '201', '021']
t = int(input())
print(a[n % len(a)][t])
