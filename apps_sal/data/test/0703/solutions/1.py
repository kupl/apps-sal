k,a,b,v = list(map(int,input().split()))

sections = (a-1)//v+1

full_boxes = b//(k-1)
partial_box_sections = b % (k-1) + 1

boxes_used = 0;

if sections <= full_boxes*k:
    boxes_used += (sections-1)//k+1
    sections = 0
else:
    sections -= full_boxes*k;
    boxes_used += full_boxes
    if sections <= partial_box_sections:
        sections = 0
        boxes_used += 1
    else:
        sections -= partial_box_sections
        boxes_used += 1
        
        boxes_used += sections
        sections = 0

print(boxes_used)

