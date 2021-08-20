d = input()
d = int(d)
st1 = input()
notes = [int(i) for i in st1.split(' ')]


def unfortunate_sum(notes):
    if 1 in notes:
        print(-1)
        return
    else:
        print(1)
        return


unfortunate_sum(notes)
