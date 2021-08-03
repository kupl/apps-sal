def run():
    input()
    s = input()

    for i in range(len(s)):

        if s[i] != '?':
            if i > 0 and s[i - 1] == s[i]:
                return False
            if i < len(s) - 1 and s[i + 1] == s[i]:
                return False
            continue

    for i in range(len(s)):
        if s[i] != '?':
            continue
        if i == 0:
            return True
        if i == len(s) - 1:
            return True

        if s[i - 1] == s[i] or s[i + 1] == s[i]:
            return True

        if s[i - 1] == s[i + 1]:
            return True

    return False


print('Yes' if run() else 'No')
