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

    n = read_int()
    nums = read_int_array()
    out = nums[0]
    first = nums[0]
    for i in range(1, n):
        out = min(out, min(nums[i], first) // i)
    last = nums[-1]
    for i in range(n-2, 0, -1):
        out = min(out, min(nums[i], last) // (n-1 - i))
    write(out)

main()

