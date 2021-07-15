s = input()

if len(s) <= 5:
    print(0)
else:
    words = set()
    s = s[5:]
    r = len(s)

    if r == 4:
        words.add(s[1:])
        words.add(s[2:])
        words.add(s[:2])

    if r == 2:
        words.add(s)

    if r == 3:
        words.add(s)
        words.add(s[1:])

    s = s[::-1]

    if r > 4:
        dp2 = [0 for _ in range(r)]
        dp3 = [0 for _ in range(r)]
        dp2[1] = 1
        dp3[2] = 1

        words.add(s[:2][::-1])
        words.add(s[:3][::-1])
        for i in range(3, r):
            if dp2[i - 2] and s[i - 3:i - 1] != s[i - 1:i + 1]:
                dp2[i] = 1
                words.add(s[i - 1:i + 1][::-1])

            if dp2[i - 3] and i - 4 >= 0 and s[i - 4:i - 2] != s[i - 2:i + 1]:
                dp3[i] = 1
                words.add(s[i - 2:i + 1][::-1])

            if dp3[i - 2] and i - 4 >= 0 and s[i - 4:i - 1] != s[i - 1:i + 1]:
                dp2[i] = 1
                words.add(s[i - 1:i + 1][::-1])

            if dp3[i - 3] and i - 5 >= 0 and s[i - 5:i - 2] != s[i - 2:i + 1]:
                dp3[i] = 1
                words.add(s[i - 2:i + 1][::-1])

    print(len(words))
    for word in sorted(words):
        print(word)
