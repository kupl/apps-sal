def main():
    t = int(input())
    for i in range(t):
        s = input()
        const = len(s)
        ans = set()
        i = 0
        while i < const:
            if i + 4 < const:
                if s[i:i + 5] == 'twone':
                    ans.add(str(i + 3))
                    i += 3
                elif i + 2 < const:
                    if s[i:i + 3] == 'one':
                        ans.add(str(i + 2))
                    if s[i:i + 3] == 'two':
                        ans.add(str(i + 2))
            elif i + 2 < const:
                if s[i:i + 3] == 'one':
                    ans.add(str(i + 2))
                if s[i:i + 3] == 'two':
                    ans.add(str(i + 2))
            i += 1
        print(len(ans))
        print(' '.join(ans))


main()
