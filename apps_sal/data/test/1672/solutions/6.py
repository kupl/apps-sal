n = int(input())
sum = 0
magnet = 0
for i in range(n):
    magneti = input()
    if magneti != magnet:
        sum += 1
        magnet = magneti
print(sum)
