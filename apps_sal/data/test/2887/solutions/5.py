n = int(input())
vol = list(map(int, input().split()))
temp = list(map(int, input().split()))

i = 0
count = 0

while i < len(temp):
    j = i
    count = 0
    while j >= 0 and i < len(temp):

        if vol[j] < temp[i] and vol[j] != 0:
            count += vol[j]
            vol[j] = 0
            #print(count,end= ' ')

        elif vol[j] >= temp[i] and vol[j] != 0:
            vol[j] = vol[j] - temp[i]
            count += temp[i]
        j -= 1
    print(count, end=" ")

    i += 1
