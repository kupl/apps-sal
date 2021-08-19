import sys
sys_in = input()


def counter(dna):
    count = 1
    even_count = 0
    previous = dna[0]
    dna = dna[1:]
    while dna != '':
        if dna[0] == previous:
            count += 1
        else:
            previous = dna[0]
            if count % 2 == 0:
                even_count += 1
            count = 1
        dna = dna[1:]
    if count % 2 == 0 and count != 0:
        even_count += 1
    return even_count


print(str(counter(sys_in)) + '\n')
