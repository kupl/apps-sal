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
    counts = {}
    import collections
    inv_counts = collections.defaultdict(int)
    out = 0
    for i, x in enumerate(nums):
        c = inv_counts[x]
        if c:
            counts[c].remove(x)
            if not counts[c]:
                counts.pop(c)
        c += 1
        inv_counts[x] = c
        counts.setdefault(c, set()).add(x)
        if len(counts) == 2 and any(len(s) == 1 and ((k-1 in counts) or k == 1) for k, s in list(counts.items())):
            out = i + 1
        elif len(counts) == 1:
            k = next(iter(list(counts.keys())))
            if k == 1 or len(counts[k]) == 1:
                out = i + 1
    write(out)

main()

