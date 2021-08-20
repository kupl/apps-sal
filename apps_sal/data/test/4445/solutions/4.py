n = int(input())
A = list(map(int, input().split()))
chet = []
nechet = []
for i in A:
    if i % 2 == 0:
        chet.append(i)
    else:
        nechet.append(i)
if len(chet) == len(nechet) or abs(len(chet) - len(nechet)) == 1:
    print(0)
elif len(chet) > len(nechet):
    print(sum(sorted(chet)[:len(chet) - len(nechet) - 1]))
else:
    print(sum(sorted(nechet)[:len(nechet) - len(chet) - 1]))
