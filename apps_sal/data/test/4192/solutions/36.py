import re
import sys

# Lista de Entradas
lst = []
for line in sys.stdin:
    lst.append(line.rstrip("\n"))


regex = [[int(r) for r in re.findall("(\d+)", line)]
         for line in lst]

verifica = lambda x: "No" if x[0] / x[2] > x[1] else "Yes"


[print(verifica(r)) for r in regex]
