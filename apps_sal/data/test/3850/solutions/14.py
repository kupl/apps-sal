filler = [0] * 10000

numbers = list(map(int, input().split()))

n = numbers[0]
k = numbers[1]
p = numbers[2]

rezultat = 9999999999999999

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

#a = a + filler
#b = b + filler

for i in range(k - n + 1):
    temp_max = -999999999
    for j in range(n):
        temp_max =  max(abs(b[i + j] - a[j]) + abs(b[i + j] - p), temp_max)
        
    rezultat = min(temp_max, rezultat)
    
print(rezultat)



