def main():
    try:
        while True:
            s = input()
            if len(s) < 26:
                print(-1)
                continue
            fq = [0] * 26
            bad_count = 0
            for c in s[:26]:
                if c != '?':
                    c = ord(c) - 65
                    fq[c] += 1
                    if fq[c] == 2:
                        bad_count += 1

            def check(pos):
                if bad_count > 0:
                    return False
                ls = list(s)
                cur = 0
                for (i, c) in enumerate(s[pos - 26:pos], pos - 26):
                    if c == '?':
                        while fq[cur] > 0:
                            assert fq[cur] == 1
                            cur += 1
                        ls[i] = chr(cur + 65)
                        fq[cur] = 1
                print(''.join(ls).replace('?', 'A'))
                return True
            for (i, c) in enumerate(s[26:], 26):
                if check(i):
                    break
                if s[i - 26] != '?':
                    c0 = ord(s[i - 26]) - 65
                    fq[c0] -= 1
                    if fq[c0] == 1:
                        bad_count -= 1
                if c != '?':
                    c = ord(c) - 65
                    fq[c] += 1
                    if fq[c] == 2:
                        bad_count += 1
            else:
                if not check(len(s)):
                    print(-1)
    except EOFError:
        pass


main()
