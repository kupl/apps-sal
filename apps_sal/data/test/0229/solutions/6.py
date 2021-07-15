3

n = int(input())
array = list(set(list(map(int, input().split()))))
array.sort()

if len(array) < 3:
    print("YES")
elif len(array) > 3 or array[1] - array[0] != array[2] - array[1]:
    print("NO")
else:
    print("YES")


