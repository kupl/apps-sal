kassa = int(input())
people = list(map(int, input().split()))
number = []
for i in range(len(people)):
    number.append(list(map(int, input().split())))
for i in range(len(number)):
    number[i] = sum(number[i]) * 5 + len(number[i]) * 15
print(min(number))
