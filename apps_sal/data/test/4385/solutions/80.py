num = [int(input()) for i in range(5)]
k = int(input())
x = 'Yay!'
for h in num:
    for j in num:
        if k < j - h:
            x = ':('
print(x)
