s = input()
n = ['Sunny', 'Cloudy', 'Rainy']
for i in range(2):
    if s == n[i]:
        print(n[i + 1])
if s == 'Rainy':
    print('Sunny')
