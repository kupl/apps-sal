N = int(input())

keta = []
for i in range(1,N+1):
    keta.append(len(str(i)))

odd = list(filter(lambda n: n % 2 == 1, keta))
print(len(odd))
