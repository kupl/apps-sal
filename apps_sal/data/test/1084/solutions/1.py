# python3

def readline(): return tuple(map(int, input().split()))


def main():
    n, m = readline()
    unique_rows = list()

    first_occ = [None] * m

    while n:
        n -= 1
        row = input()
        saved = None
        for (i, char) in enumerate(row):
            if char == '#':
                if first_occ[i] is not None:
                    if row != unique_rows[first_occ[i]]:
                        return False
                    else:
                        break
                else:
                    if saved is None:
                        unique_rows.append(row)
                        saved = len(unique_rows) - 1
                    first_occ[i] = saved
            else:
                assert char == '.'

    return True


print("Yes" if main() else "No")
