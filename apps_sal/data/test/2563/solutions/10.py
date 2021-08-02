for _ in range(int(input())):
    a = list(input())
    odd = []
    even = []
    for elem in a:
        elem = int(elem)
        if elem % 2 == 0:
            even.append(elem)
        else:
            odd.append(elem)
    i = 0
    j = 0
    output = []
    for _ in range(len(a)):
        if i == len(odd):
            output.append(str(even[j]))
            j += 1
        elif j == len(even):
            output.append(str(odd[i]))
            i += 1
        else:
            if odd[i] < even[j]:
                output.append(str(odd[i]))
                i += 1
            else:
                output.append(str(even[j]))
                j += 1
    print("".join(output))
