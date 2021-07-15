S_list = list(map(int,input().split()))

A, B = S_list[0], S_list[1]
if (A * B * (A + B)) % 3 == 0 :
    result = "Possible"
else:
    result = "Impossible"
print(result)

