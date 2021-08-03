S = input()
K = int(input())


def main():
    cnt = 1
    for i in S:
        if i == '1':
            if K == cnt:
                return '1'
            else:
                cnt += 1
                continue
        else:
            return i
        return '1'


print(int(main()))
