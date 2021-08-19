# Enter your code here. Read input from STDIN. Print output to STDOUT
import xml.etree.ElementTree as etree
xml_str = ""
n = int(input())
for i in range(0, n):
    tmp_str = input()
    xml_str = xml_str + tmp_str

tree = etree.ElementTree(etree.fromstring(xml_str))
root = tree.getroot()
ar = []


def cnt_node(node):
    return max([0] + [cnt_node(child) + 1 for child in node])


cnt = cnt_node(root)
print(cnt)
