def main():
    from sys import stdin, stdout

    def read():
        return stdin.readline().rstrip('\n')

    def read_array(sep=None, maxsplit=-1):
        return read().split(sep, maxsplit)

    def read_int():
        return int(read())

    def read_int_array(sep=None, maxsplit=-1):
        return [int(a) for a in read_array(sep, maxsplit)]

    def write(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in args) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in array) + end)

    n, z = read_int_array()
    nums = read_int_array()
    nums.sort()

    out = 0
    used = [False] * n
    i, j = 0, len(nums) // 2
    while i < n:
        used[i] = True
        while j < n and (used[j] or (nums[j] - nums[i] < z)):
            j += 1
        if j == n:
            break
        used[j] = True
        while i < n and used[i]:
            i += 1
        out += 1
    write(out)


main()
