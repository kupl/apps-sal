def sorting(string, string1):
    if len(string) > len(string1):
        string = string[:len(string1)]
    for q in range(len(string)):
        if string[q] > string1[q]:
            string = string[:q]
            break
    return string


n = int(input())
array = [str(input()) for c in range(n)]
b = n - 2
while b > -1:
    if array[b + 1] >= array[b]:
        b = b - 1
    else:
        array[b] = sorting(array[b], array[b + 1])
print("\n".join(array))
