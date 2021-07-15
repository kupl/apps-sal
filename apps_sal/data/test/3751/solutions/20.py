
def main():
    code = str(input())

    curr_a = 'a'
    while code:
        if code[0] != curr_a:
            print('NO')
            return
        code  = code.replace(curr_a, '')
        curr_a = chr(ord(curr_a) + 1)
    print('YES')
    return
main()
