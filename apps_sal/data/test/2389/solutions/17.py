
def main():
    N, A, B, C = list(map(int, input().split()))
    array = [A, B, C]
    string = ['A', 'B', 'C']
    si = []
    if A + B + C <= 0:
        print('No')
        return
    for _ in range(N):
        s = input()
        si += (0 if s == 'AB' else 1 if s == 'BC' else 2),

    ans = []
    for i in range(len(si)):
        s = si[i]
        index = -3 if s == 0 else -2 if s == 1 else -1
        if array[index] == 0:
            array[index] += 1
            array[index + 1] -= 1
            ans += string[index],
        elif array[index + 1] == 0:
            array[index] -= 1
            array[index + 1] += 1
            ans += string[index + 1],
        elif array[index] == 1 and array[index + 1] == 1:
            if i + 1 >= len(si):
                array[index] += 1
                array[index + 1] -= 1
                ans += string[index],
            else:
                if si[i + 1] != (index + 1) % 3:
                    array[index] += 1
                    array[index + 1] -= 1
                    ans += string[index],
                else:
                    array[index] -= 1
                    array[index + 1] += 1
                    ans += string[index + 1],
        elif array[index] == 1:
            array[index] += 1
            array[index + 1] -= 1
            ans += string[index],
        else:
            array[index] -= 1
            array[index + 1] += 1
            ans += string[index + 1],

        if array[0] < 0 or array[1] < 0 or array[2] < 0:
            print('No')
            return

    print('Yes')
    for s in ans:
        print(s)


main()
